from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot, retreat_free_when
from ptcgo.game.card_effects.support_common import entity_name


def _unown_named(pokemon):
    return pokemon is not None and "Unown" in entity_name(pokemon)


def _zoom(pokemon, carrier):
    from ptcgo.game.session.passives import carrier_pokemon

    holder = carrier_pokemon(carrier) or carrier
    if pokemon is None or holder is None:
        return False
    if pokemon.owning_player_id != holder.owning_player_id:
        return False
    if not _unown_named(pokemon):
        return False
    return not is_in_active_spot(holder)


card = PokemonCardDef(
    guid="6a685e34-cd42-5261-be19-c18db6bb6872",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownZ.Name",
    display_name="Unown [Z]",
    searchable_by=["Unown [Z]", "Basic", "UnownZ"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Zoom]",
            game_text="As long as Unown [Z] is Benched, you pay no Energy cost to retreat a Pok\u00e9mon with Unown in its name.",
            passive=retreat_free_when(_zoom),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)