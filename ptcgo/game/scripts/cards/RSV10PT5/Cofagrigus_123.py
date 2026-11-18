from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a603c8e4-310e-5321-b16f-893d736fc81c",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Cofagrigus"],
    subtypes=["Stage 1"],
    collector_number=123,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Attack(
            title="Extended Damagriiigus",
            game_text="Move all damage counters from 1 of your Benched Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)