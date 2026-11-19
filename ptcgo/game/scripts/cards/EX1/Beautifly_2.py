from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.session.passives import Passive
from ptcgo.game.card_effects.attacks_common import condition_attack

class WitheringDustPassive(Passive):
    """As long as Beautifly is in play, do not apply Resistance for any Active Pokemon."""

    def modify_resistance(self, calc, carrier):
        target = calc.target
        if target is not None and is_in_active_spot(target):
            calc.resistance_applies = False

card = PokemonCardDef(
    guid="bfaeb3d5-656e-526a-aaae-ff013d28bc44",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Withering Dust",
            game_text="As long as Beautifly is in play, do not apply Resistance for all Active Pok\u00e9mon.",
            passive=WitheringDustPassive(),
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Parallel Gain",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon, including Beautifly.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)