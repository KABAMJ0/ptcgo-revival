from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b2b9510-122a-53c3-8fc3-7f100c8294cf",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=101,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Emergency Rotation",
            game_text="Once during your turn, if this Pok\u00e9mon is in your hand and your opponent has any Stage 2 Pok\u00e9mon in play, you may put this Pok\u00e9mon onto your Bench.",
            effect=self_energy_discard_attack(all_energy=True),
        ),
        Attack(
            title="Hyper Ray",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)