from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c34dc9cf-8e2f-5e55-87cd-d52882c195be",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=95,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Daunting Gaze",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Item cards from their hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Cracking Stomp",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)