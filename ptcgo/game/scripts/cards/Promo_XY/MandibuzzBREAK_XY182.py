from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID, CardType

async def wings_of_disaster(ctx):
    """20 to each opposing Pokemon (no Weakness/Resistance), then discard every
    Pokemon Tool attached to them."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        tools = [c for c in (getattr(pokemon, "children", None) or [])
                 if c.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value]
        if tools:
            await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="c99e8ffc-d3dd-515a-93ed-c1bdfd353634",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MandibuzzBREAK.Name",
    display_name="Mandibuzz BREAK",
    searchable_by=["Mandibuzz BREAK", "BREAK", "MandibuzzBREAK"],
    subtypes=["BREAK"],
    collector_number=182,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    family_id=630,
    abilities=[
        Attack(
            title="Wings of Disaster",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. Don't apply Weakness and Resistance. Discard all Pok\u00e9mon Tool cards attached to each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=wings_of_disaster,
        ),
    ],
)