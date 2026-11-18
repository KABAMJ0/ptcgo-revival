from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cda0654d-0a0b-50d5-970c-4a5907e79f8c",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper",
    searchable_by=["Pelipper", "Stage 1", "Pelipper"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=279,
    abilities=[
        Ability(
            title="Hearsay",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may choose 1: put a Supporter card from your discard pile into your hand; or search your deck for a Supporter card, reveal it, put it into your hand, and then shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)