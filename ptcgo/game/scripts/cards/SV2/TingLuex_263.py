from ptcgo.game.card_effects.attacks_common import bench_counter_picks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.card_effects.pokemon import is_pokemon_ex
from ptcgo.game.card_effects.passives_common import ability_lock_passive, is_in_active_spot
from ptcgo.game.attributes import AttrID

def _cursed_land_target(pokemon, carrier):
    """An opposing Pokemon in play that has any damage counters on it, other
    than a Pokemon ex, while this card's holder is the Active."""
    holder = carrier_pokemon(carrier)
    if holder is None or not is_in_active_spot(holder):
        return False
    if pokemon.owning_player_id == carrier.owning_player_id:
        return False
    if is_pokemon_ex(pokemon):
        return False
    current = pokemon.get_attribute(AttrID.HP) or 0
    printed = pokemon.attribute_originals.get(AttrID.HP.value, current)
    return current < printed

card = PokemonCardDef(
    guid="a8e2e335-c641-553c-962f-705cfbe753a7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TingLuex.Name",
    display_name="Ting-Lu ex",
    searchable_by=["Ting-Lu ex", "Basic", "ex", "TingLuex"],
    subtypes=["Basic", "ex"],
    collector_number=263,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=1003,
    abilities=[
        Ability(
            title="Cursed Land",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Pok\u00e9mon in play that have any damage counters on them have no Abilities, except for Pok\u00e9mon ex.",
            passive=ability_lock_passive(_cursed_land_target),
        ),
        Attack(
            title="Land Scoop",
            game_text="Put 2 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=150,
            effect=bench_counter_picks(1, 2),
        ),
    ],
)