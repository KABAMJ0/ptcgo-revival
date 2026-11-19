from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_per_heads
from ptcgo.game.card_effects.passives_common import hp_bonus_tool
from ptcgo.game.models.board import BoardState
from ptcgo.game.session.effects import is_special_energy


def _has_special_energy(pokemon) -> bool:
    return any(is_special_energy(energy)
               for energy in BoardState.attached_energies(pokemon))


card = PokemonCardDef(
    guid="e2588676-6eb2-58ac-b215-12f7cfdeaa93",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name",
    display_name="Tyrantrum",
    searchable_by=["Tyrantrum", "Stage 2", "Tyrantrum"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    family_id=696,
    abilities=[
        Ability(
            title="Tyrannically Gutsy",
            game_text="If this Pok\u00e9mon has any Special Energy attached, it gets +150 HP.",
            passive=hp_bonus_tool(150, holder_pred=_has_special_energy),
        ),
        Attack(
            title="Wreak Havoc",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=mill_per_heads(1, opponent=True),
        ),
    ],
)