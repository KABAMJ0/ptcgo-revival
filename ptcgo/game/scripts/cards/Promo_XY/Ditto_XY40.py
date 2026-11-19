from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card
from ptcgo.game.card_effects.passives_common import attack_grant_passive, is_in_active_spot

def _opponent_active_sources(board, pokemon, carrier):
    """The opponent's Active Pokemon, whose printed attacks this may use.

    The board hands no session here, so walk its entity cache for the opposing
    Pokemon whose parent area is the Active spot."""
    from ptcgo.game.models.board import PokemonEntity
    mine = pokemon.owning_player_id
    for entity in list(getattr(board, "_entity_cache", {}).values()):
        if (isinstance(entity, PokemonEntity) and entity.owning_player_id != mine
                and is_in_active_spot(entity)):
            return [entity]
    return []


card = PokemonCardDef(
    guid="ad9d7205-fd76-5fda-80c2-6f9cddae0abe",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Metamorphosis Gene",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, it can use the attacks of your opponent's Active Pok\u00e9mon. (You still need the necessary Energy to use each attack.)",
            passive=attack_grant_passive(_opponent_active_sources),
        ),
        Attack(
            title="Stick On",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=attach_from_discard(is_basic_energy_card, count=1, target="self"),
        ),
    ],
)