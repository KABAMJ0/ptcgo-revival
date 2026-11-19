from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_special_energy


async def _delta_moon(ctx):
    """When the opponent attaches a Special Energy from hand, 1 damage counter
    on the Pokemon that received it."""
    receiver = ctx.energy_receiver
    energy = ctx.attached_energy
    if ctx.attaching_player_id != ctx.opponent_id or receiver is None:
        return
    if energy is None or not is_special_energy(energy):
        return
    await ctx.deal_damage(10, target=receiver, apply_modifiers=False,
                          as_counters=True)


card = PokemonCardDef(
    guid="84c3dfc3-4627-54ce-8df0-27976b5a9f2b",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon δ",
    searchable_by=["Umbreon \u03b4", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Delta Moon",
            game_text="When your opponent attaches a Special Energy card from his or her hand to 1 of his or her Pok\u00e9mon, put 1 damage counter on that Pok\u00e9mon. You can't use more than 1 Delta Moon Pok\u00e9-Body each turn.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            shared_once_per_turn="Delta Moon",
            effect=_delta_moon,
        ),
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.METAL: 1},
            effect=snipe_attack(30, pool="any", apply_modifiers=False),
        ),
    ],
)