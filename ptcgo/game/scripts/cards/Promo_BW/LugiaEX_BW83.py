from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _extra_prize(ctx):
    """The opponent takes 1 more Prize card(s) if this attack Knocks Out their Active."""
    ctx.add_extra_prize_watcher(prizes=1)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="ceee9100-e4b7-54d7-9874-15f56f1808f1",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name",
    display_name="Lugia-EX",
    searchable_by=["Lugia-EX", "Basic", "EX", "Team Plasma", "LugiaEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=83,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Ability(
            title="Overflow",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from an attack of this Pok\u00e9mon, take 1 more Prize card.",
            effect=_extra_prize,
        ),
        Attack(
            title="Plasma Gale",
            game_text="Discard a Plasma Energy attached to this Pok\u00e9mon. If you can't discard a Plasma Energy, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=unimplemented,
        ),
    ],
)