from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import takes_less_passive


def _has_energy(pokemon, carrier):
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    return bool(pokemon.children)


_ultra_thick_skin = takes_less_passive(10, protects=_has_energy)

card = PokemonCardDef(
    guid="1d92f887-24ae-5a8d-8398-9e6a1d2eea2d",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    display_name="Phanpy",
    searchable_by=["Phanpy", "Basic", "Phanpy"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="COL",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=231,
    abilities=[
        Ability(
            title="Ultra-Thick Skin",
            game_text="As long as Phanpy has Energy attached to it, any damage done to Phanpy by attacks is reduced by 10 (after applying Weakness and Resistance).",
            passive=_ultra_thick_skin,
        ),
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(30)),
        ),
    ],
)