from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d8a4d79-2dea-59e4-a6c2-a27d7cb9dacd",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=75,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Intensifying Burn",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=mill_attack(3, opponent=False),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)