from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="45118137-2462-5818-bd1b-3540250730d1",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    display_name="Metapod",
    searchable_by=["Metapod", "Stage 1", "Metapod"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Defensive Posture",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=flip_protection(prevent=True),
        ),
    ],
)