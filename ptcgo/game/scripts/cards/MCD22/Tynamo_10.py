from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import retreat_free_when
from ptcgo.game.models.board import BoardState


def _has_any_energy(pokemon, carrier):
    return pokemon is carrier and bool(BoardState.attached_energies(pokemon))


card = PokemonCardDef(
    guid="8ea63455-4990-5693-8a7c-e988ecc1aecf",
    key="MCD22",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="MCD22",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Ability(
            title="Levitate",
            game_text="If this Pok\u00e9mon has any Energy attached, it has no Retreat Cost.",
            passive=retreat_free_when(_has_any_energy),
        ),
        Attack(
            title="Tiny Charge",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)