from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def chrono_burst(ctx):
    """80; you may shuffle all Energy attached to this Pokemon into your deck
    to do 80 more."""
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies and await ctx.ask_yes_no(
            "Shuffle all Energy attached to this Pokémon into your deck "
            "to do 80 more damage?"):
        await ctx.shuffle_into_deck(energies, ctx.player_id)
        await ctx.deal_damage(160)
        return
    await ctx.deal_damage(80)


card = PokemonCardDef(
    guid="201e706f-00a8-568c-941b-09da13c756be",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=483,
    abilities=[
        Attack(
            title="Beam",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
        Attack(
            title="Chrono Burst",
            game_text="You may shuffle all Energy attached to this Pok\u00e9mon into your deck and have this attack do 80 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=chrono_burst,
        ),
    ],
)