from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.passives_common import Passive
from ptcgo.game.models.board import PlayArea
from ptcgo.game.session.passives import carrier_pokemon


def _prizes_left(pokemon):
    node = pokemon
    while node is not None and type(node).__name__ != "PlayerEntity":
        node = getattr(node, "parent", None)
    if node is None:
        return None
    for child in node.children:
        if isinstance(child, PlayArea) and child.get_attribute(AttrID.NAME) == "prizePile":
            return len(child.children)
    return None


class _AirheadPassive(Passive):
    """At 2, 4 or 6 Prize cards left this Pokemon can't attack. The engine's
    blocks_attack hook carries no board, so the prize count is read from the
    carrier's own player entity."""

    def blocks_attack(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        return _prizes_left(pokemon) in (2, 4, 6)

card = PokemonCardDef(
    guid="de031d20-043f-572a-8c72-4a6f8ae0ffde",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Airhead",
            game_text="If you have 2, 4, or 6 Prize Cards left, this Pok\u00e9mon can't attack.",
            passive=_AirheadPassive(),
        ),
        Attack(
            title="Lazy Headbutt",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)