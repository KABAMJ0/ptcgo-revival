from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="10a5d66e-0475-56c0-9eb2-d3dea36eff55",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaKangaskhanex.Name",
    display_name="Mega Kangaskhan ex",
    searchable_by=["Mega Kangaskhan ex", "Basic", "MEGA", "ex", "MegaKangaskhanex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=164,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Ability(
            title="Run Errand",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may use this Ability. Draw 2 cards. You can't use more than 1 Run Errand Ability each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Rapid-Fire Combo",
            game_text="Flip a coin until you get tails. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            damage_operator="+",
            effect=flip_damage(until_tails=True, per_heads=50, base=200),
        ),
    ],
)