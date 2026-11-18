from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d7d80271-36d1-525f-a427-805d60ef4083",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2", "Tinkaton"],
    subtypes=["Stage 2"],
    collector_number=140,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=959,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Wild Press",
            game_text="This Pok\u00e9mon also does 60 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=unimplemented,
        ),
    ],
)