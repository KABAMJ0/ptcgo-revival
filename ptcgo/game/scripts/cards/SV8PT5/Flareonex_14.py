from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="0d35e76a-5129-50f7-9b85-6284dd4a7600",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareonex.Name",
    display_name="Flareon ex",
    searchable_by=["Flareon ex", "Stage 1", "Tera", "ex", "Flareonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=14,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Burning Charge",
            game_text="Search your deck for up to 2 Basic Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=search_attach_energy(is_basic_energy_card, count=2, distribute=False),
        ),
        Attack(
            title="Carnelian",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=280,
            effect=lock_self_attack(),
        ),
    ],
)