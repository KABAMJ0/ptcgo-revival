from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab9d4056-05b7-59ef-ba0d-3c5bdbbcc158",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Blizzard Veil",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Benched Water Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Cold Cyclone",
            game_text="Move 2 Water Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)