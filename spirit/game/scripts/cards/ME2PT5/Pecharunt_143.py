from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b275d387-d70d-5e18-a6b5-c47583b02686",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pecharunt.Name",
    display_name="Pecharunt",
    searchable_by=["Pecharunt", "Basic", "Pecharunt"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1025,
    abilities=[
        Ability(
            title="Final Chain",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Mochi Rush",
            game_text="During your next turn, this Pok\u00e9mon's Mochi Rush attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)