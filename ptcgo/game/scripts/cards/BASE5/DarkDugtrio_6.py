from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_choice

from ptcgo.game.session.passives import Passive


class SinkholePassive(Passive):
    """Whenever the opponent's Active retreats, they flip a coin; on tails it
    takes 20 damage with no Weakness or Resistance."""

    async def on_retreat(self, ctx, pokemon, carrier):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return
        heads = await ctx.flip_coins(1, "Sinkhole")
        if not (heads and heads[0]):
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


def _sinkhole():
    """Whenever your opponent's Active Pokemon retreats, your opponent flips a
    coin; on tails this power does 20 damage to that Pokemon."""
    return SinkholePassive()

card = PokemonCardDef(
    guid="b02495ba-7e3a-5563-89d2-095b527d9e9d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkDugtrio.Name",
    display_name="Dark Dugtrio",
    searchable_by=["Dark Dugtrio", "Stage 1", "DarkDugtrio"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Sinkhole",
            game_text="Whenever your opponent's Active Pok\u00e9mon retreats, your opponent flips a coin. If tails, this power does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power stops working while Dark Dugtrio is Asleep, Confused, or Paralyzed.",
            passive=_sinkhole(),
        ),
        Attack(
            title="Knock Down",
            game_text="Your opponent flips a coin. If tails, this attack does 20 damage plus 20 more damage; if heads, this attack does 20 damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="+",
            effect=flip_choice(heads=20, tails=40),
        ),
    ],
)