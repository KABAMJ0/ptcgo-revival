from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import smokescreen_attack


card = PokemonCardDef(
    guid="90a7fc48-30e5-5da4-9c0d-92203bbda037",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    display_name="Quaxly",
    searchable_by=["Quaxly", "Basic", "Quaxly"],
    subtypes=["Basic"],
    collector_number=206,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=912,
    abilities=[
        Attack(
            title="Apply Gel",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=smokescreen_attack(),
        ),
    ],
)