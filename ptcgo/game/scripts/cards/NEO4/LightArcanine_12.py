from ptcgo.game.data_utils import def_for
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.support_common import opponent_switches


async def _drive_off(ctx):
    """Drive Off: they pick a Benched Pokemon and swap it into the Active."""
    await opponent_switches(ctx)


async def _gentle_flames(ctx):
    """Gentle Flames: 10 against a Baby, 30 against a Basic, else 50."""
    defender = ctx.defender
    if defender is None:
        return
    subtypes = [str(s) for s in (getattr(def_for(defender.archetype_id),
                                        "subtypes", None) or [])]
    if any("Baby" in s for s in subtypes):
        await ctx.deal_damage(10)
    elif any("Basic" in s for s in subtypes):
        await ctx.deal_damage(30)
    else:
        await ctx.deal_damage(50)


def _display_name(entity) -> str:
    """The printed name of a card on the board (empty when unknown)."""
    return getattr(def_for(getattr(entity, "archetype_id", "") or ""),
                   "display_name", "") or ""

card = PokemonCardDef(
    guid="8af232ef-b7e8-5499-9acf-1185e589e2c2",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightArcanine.Name",
    display_name="Light Arcanine",
    searchable_by=["Light Arcanine", "Stage 1", "LightArcanine"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Drive Off",
            game_text="As long as Light Arcanine is your Active Pok\u00e9mon, once during your turn (before your attack), if your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. This power can't be used while Light Arcanine is Asleep, Confused, or Paralyzed.",
            effect=_drive_off,
        ),
        Attack(
            title="Gentle Flames",
            game_text="If the Defending Pok\u00e9mon is a Baby Pok\u00e9mon, this attack does 10 damage instead of 50. If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, this attack does 30 damage instead of 50.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_gentle_flames,
        ),
    ],
)