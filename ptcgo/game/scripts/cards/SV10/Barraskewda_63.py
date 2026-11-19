from ptcgo.game.card_effects.passives_common import flip_protection
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eba50dfd-90d7-5c34-966e-d01cfeb1aeeb",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name",
    display_name="Barraskewda",
    searchable_by=["Barraskewda", "Stage 1", "Barraskewda"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    family_id=846,
    abilities=[
        Attack(
            title="Sharp Fin",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Dive",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)