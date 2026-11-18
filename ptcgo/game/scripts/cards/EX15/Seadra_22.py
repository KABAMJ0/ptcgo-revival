from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import smokescreen_attack

card = PokemonCardDef(
    guid="ece1824d-cc6d-53c4-9e50-6fcdc7276701",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra δ",
    searchable_by=["Seadra \u03b4", "Stage 1", "Seadra"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=117,
    abilities=[
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)