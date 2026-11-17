from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d296e3d0-6181-5615-a933-c73a9097bc8b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysStarly.Name",
    display_name="Larry's Starly",
    searchable_by=["Larry's Starly", "Basic", "LarrysStarly"],
    subtypes=["Basic"],
    collector_number=168,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=396,
    abilities=[
        Attack(
            title="Minor Errand-Running",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)