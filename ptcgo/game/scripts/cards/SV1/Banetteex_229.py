from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fc245138-9497-58ab-b77a-c0f563ade1b4",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banetteex.Name",
    display_name="Banette ex",
    searchable_by=["Banette ex", "Stage 1", "ex", "Banetteex"],
    subtypes=["Stage 1", "ex"],
    collector_number=229,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Everlasting Darkness",
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 60 damage for each Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)