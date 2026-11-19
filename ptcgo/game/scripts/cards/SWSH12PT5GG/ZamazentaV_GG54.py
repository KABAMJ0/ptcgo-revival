from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_prizes_taken, damage_per
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.attacks_common import damage_per, count_prizes_taken

async def regal_stance(ctx):
    """Once per turn: discard your hand and draw 5 cards. Ends your turn."""
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(5)

card = PokemonCardDef(
    guid="7e8e2e36-d2fd-5655-bb26-46afc9626172",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZamazentaV.Name",
    display_name="Zamazenta V",
    searchable_by=["Zamazenta V", "Basic", "V", "ZamazentaV"],
    subtypes=["Basic", "V"],
    collector_number=54,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=889,
    abilities=[
        Ability(
            title="Regal Stance",
            game_text="Once during your turn, you may discard your hand and draw 5 cards. If you use this Ability, your turn ends.",
            effect=regal_stance,
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("theirs"), 30, base=120),
        ),
    ],
)