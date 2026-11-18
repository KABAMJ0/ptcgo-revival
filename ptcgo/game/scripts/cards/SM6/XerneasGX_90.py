from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c4ffe62-3823-5057-8ed0-06092d49c86c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XerneasGX.Name",
    display_name="Xerneas-GX",
    searchable_by=["Xerneas-GX", "Basic", "GX", "XerneasGX"],
    subtypes=["Basic", "GX"],
    collector_number=90,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=716,
    abilities=[
        Attack(
            title="Overrun",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Horns",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Sanctuary-GX",
            game_text="Move all damage counters from each of your Pok\u00e9mon to your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)