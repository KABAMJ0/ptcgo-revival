from ptcgo.game.card_effects.passives_common import Passive
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class _DualArmorPassive(Passive):
    """With any Metal Energy attached, this Pokemon is Fighting AND Metal."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        if any(energy_provides_type(e, PokemonTypes.METAL.value)
               for e in (pokemon.children or [])):
            return [PokemonTypes.FIGHTING.value, PokemonTypes.METAL.value]
        return types


card = PokemonCardDef(
    guid="0c4c6021-054d-5264-8202-8d4cb6872604",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="If this Pok\u00e9mon has any Metal Energy attached to it, this Pok\u00e9mon's type is both Fighting and Metal.",
            passive=_DualArmorPassive(),
        ),
        Attack(
            title="Hurricane Kick",
            game_text="Does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)