from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db1cd409-6d29-5f8c-bb02-f11f6791db9f",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyuremex.Name",
    display_name="Kyurem ex",
    searchable_by=["Kyurem ex", "Basic", "ex", "Kyuremex"],
    subtypes=["Basic", "ex"],
    collector_number=28,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Blizzard Burst",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon for each Prize card your opponent has taken. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)