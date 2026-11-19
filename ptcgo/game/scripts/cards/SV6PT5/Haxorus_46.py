from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.session.effects import is_special_energy


async def persist_sting(ctx):
    """If the opponent's Active has any Special Energy attached, it is Knocked Out."""
    defender = ctx.defender
    if defender is not None and any(
        is_special_energy(e) for e in ctx.attached_energies(defender)
    ):
        await ctx.knock_out(defender)


card = PokemonCardDef(
    guid="27e2e721-33ed-578c-9d35-20d35008d2b6",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Bring Down the Axe",
            game_text="If your opponent's Active Pok\u00e9mon has any Special Energy attached, it is Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=persist_sting,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=230,
            effect=mill_attack(count=3, opponent=False),
        ),
    ],
)