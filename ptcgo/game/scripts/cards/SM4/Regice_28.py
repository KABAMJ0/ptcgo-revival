from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import attack_shield_from, side_has_named


def _is_stage2(attacker) -> bool:
    return attacker is not None \
        and attacker.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value


card = PokemonCardDef(
    guid="13cd7e74-c8be-5b36-aa42-f687a828c644",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic", "Regice"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Iceberg Shield",
            game_text="If you have Regirock in play, prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Stage 2 Pok\u00e9mon.",
            passive=attack_shield_from(
                _is_stage2, effects_too=True,
                when=lambda board, carrier: side_has_named(
                    board, carrier.owning_player_id, "Regirock")),
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)