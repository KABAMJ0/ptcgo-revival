from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6d976c0-6425-5097-9cec-0c78ad81de42",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatonex.Name",
    display_name="Tinkaton ex",
    searchable_by=["Tinkaton ex", "Stage 2", "ex", "Tinkatonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=240,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Big Hammer",
            game_text="This attack does 30 damage for each card in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Pulverizing Press",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)