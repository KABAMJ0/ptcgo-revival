from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_basic_pokemon

async def _borne_ashore(ctx):
    pool = [card for card in list(ctx.discard_pile())
            + list(ctx.discard_pile(ctx.opponent_id)) if is_basic_pokemon(card)]
    if not pool:
        return
    picks = pool if len(pool) == 1 else await ctx.choose_cards(
        pool, 1, minimum=1,
        prompt="Choose a Basic Pok\u00e9mon to put onto its owner's Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="40dde91f-4344-541d-9fa5-77f488ef5897",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=594,
    abilities=[
        Attack(
            title="Borne Ashore",
            game_text="Put a Basic Pok\u00e9mon from either player's discard pile onto its owner's Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_borne_ashore,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)