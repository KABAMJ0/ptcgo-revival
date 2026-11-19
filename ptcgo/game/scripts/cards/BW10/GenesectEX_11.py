from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.card_effects.trainers import named_exactly
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, \
    unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


_PLASMA_ENERGY = named_exactly("Plasma Energy")


async def red_signal(ctx) -> None:
    """A Plasma Energy just attached from hand to this Pokemon: you may gust."""
    if ctx.energy_receiver is not ctx.source:
        return
    if ctx.attached_energy is None or not _PLASMA_ENERGY(ctx.attached_energy):
        return
    if not await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokémon with his or her "
            "Active Pokémon?"):
        return
    await gust_attack(damage_before=0)(ctx)


card = PokemonCardDef(
    guid="7bccf330-088d-53ce-9ae0-a724621cccbb",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name",
    display_name="Genesect-EX",
    searchable_by=["Genesect-EX", "Basic", "EX", "Team Plasma", "GenesectEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=11,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Ability(
            title="Red Signal",
            game_text="When you attach a Plasma Energy from your hand to this Pok\u00e9mon, you may switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=red_signal,
        ),
        Attack(
            title="Megalo Cannon",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)