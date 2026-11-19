from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack


async def sky_hunting(ctx):
    """Printed damage; if that Knocked Out the Defending Pokemon, switch this
    Pokemon with 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or defender.get_attribute(AttrID.HP, 0) > 0:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="4c36f83f-248b-5062-8352-8aa713a8353a",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=83,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Sky Hunting",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by the damage from this attack, switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=sky_hunting,
        ),
    ],
)