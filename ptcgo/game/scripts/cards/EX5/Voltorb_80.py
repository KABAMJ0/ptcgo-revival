from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53469647-a492-58c9-a38b-5462566ba494",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic", "Voltorb"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Recharge",
            game_text="Search your deck for a Lightning Energy card and attach it to Voltorb. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rolling Attack",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)