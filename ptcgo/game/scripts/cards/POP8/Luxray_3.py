from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon


class IntimidatingFangPassive(Passive):
    """While Luxray is Active, damage from the opponent's attacks is cut
    by 10 before Weakness and Resistance."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not calc.is_attack or holder is None or calc.target is None:
            return
        if calc.attacker is None \
                or calc.attacker.owning_player_id == holder.owning_player_id:
            return
        if calc.target.owning_player_id != holder.owning_player_id:
            return
        if not is_in_active_spot(holder):
            return
        calc.amount = max(0, calc.amount - 10)


async def thunder(ctx):
    await ctx.deal_damage(120)
    results = await ctx.flip_coins(1, "Thunder")
    if results and not results[0]:
        await ctx.deal_damage(40, target=ctx.attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="5a98bf51-849e-542f-87df-56d323b0f638",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="POP8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=404,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as Luxray is your Active Pok\u00e9mon, any damage done by an opponent's attack is reduced by 10 (before applying Weakness and Resistance).",
            passive=IntimidatingFangPassive(),
        ),
        Attack(
            title="Thunder",
            game_text="Flip a coin. If tails, Luxray does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=thunder,
        ),
    ],
)