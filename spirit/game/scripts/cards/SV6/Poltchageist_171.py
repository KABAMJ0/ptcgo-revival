from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="36ed7d9d-c8e9-5ec8-a3a4-93fb42c3ed4a",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    display_name="Poltchageist",
    searchable_by=["Poltchageist", "Basic", "Poltchageist"],
    subtypes=["Basic"],
    collector_number=171,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Ability(
            title="Storehouse Hideaway",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)