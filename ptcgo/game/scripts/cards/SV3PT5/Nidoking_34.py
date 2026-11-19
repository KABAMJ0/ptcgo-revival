from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
from ptcgo.game.card_effects.attacks_common import condition_attack


def _has_named_in_play(board, owner_id, name) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == name
               for p in board.pokemon_in_play(owner_id))


def _has_nidoqueen(board, pokemon, carrier) -> bool:
    return _has_named_in_play(board, carrier.owning_player_id, "Nidoqueen")

card = PokemonCardDef(
    guid="2ce556fb-0340-5012-83f1-5f99e4608125",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Enthusiastic King",
            game_text="If you have Nidoqueen in play, ignore all Energy in the costs of attacks used by this Pok\u00e9mon.",
            passive=free_attack_cost_passive(condition=_has_nidoqueen),
        ),
        Attack(
            title="Venomous Impact",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)