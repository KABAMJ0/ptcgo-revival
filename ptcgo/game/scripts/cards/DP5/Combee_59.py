from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="04fece48-72a5-56e9-bf90-03b7d7d65f14",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    display_name="Combee",
    searchable_by=["Combee", "Basic", "Combee"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=415,
    abilities=[
        Attack(
            title="Honey Scent",
            game_text="Remove 2 damage counters from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(20, scope='choice'),
        ),
        Attack(
            title="Flitter",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 2},
            effect=snipe_attack(20, pool="any", apply_modifiers=False),
        ),
    ],
)