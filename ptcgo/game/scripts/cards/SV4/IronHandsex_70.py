from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _extra_prize(ctx):
    """The opponent takes 1 more Prize card(s) if this attack Knocks Out their Active."""
    ctx.add_extra_prize_watcher(prizes=1)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="7775f48a-4a58-555c-a70f-0ef89e8e645a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronHandsex.Name",
    display_name="Iron Hands ex",
    searchable_by=["Iron Hands ex", "Basic", "ex", "Future", "IronHandsex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=70,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=992,
    abilities=[
        Attack(
            title="Arm Press",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
        Attack(
            title="Amp You Very Much",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=_extra_prize,
        ),
    ],
)