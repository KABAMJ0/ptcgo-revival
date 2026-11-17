from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4feb2f18-4ebd-5f63-a48d-5a7a427766de",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2", "Krookodile"],
    subtypes=["Stage 2"],
    collector_number=137,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Tighten Up",
            game_text="Your opponent discards 2 cards from their hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Cursed Slug",
            game_text="If your opponent has 3 or fewer cards in their hand, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)