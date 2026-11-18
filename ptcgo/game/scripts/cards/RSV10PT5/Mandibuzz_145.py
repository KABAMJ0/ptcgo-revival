from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="961814d9-805d-5ae9-bcbd-be18264f7904",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz", "Stage 1", "Mandibuzz"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    family_id=629,
    abilities=[
        Ability(
            title="Look for Prey",
            game_text="Once during your turn, you may use this Ability. Your opponent reveals their hand, and you put a Basic Pok\u00e9mon with 70 HP or less that you find there onto your opponent's Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)