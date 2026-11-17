from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="efa17d72-16d5-5828-b664-dcd8752302d8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic", "Thundurus"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Ability(
            title="Adverse Weather",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, prevent all damage done to your Benched Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Gigantic Bolt",
            game_text="This Pok\u00e9mon also does 90 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)