from ptcgo.game.card_effects.attacks_common import conditions_if, self_has_energy_of_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="da050c61-ae6a-568a-b7b6-6c02f99add87",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name",
    display_name="Simisage",
    searchable_by=["Simisage", "Stage 1", "Simisage"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    family_id=511,
    abilities=[
        Attack(
            title="Fire's Power",
            game_text="If this Pok\u00e9mon has any Fire Energy attached to it, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=conditions_if(self_has_energy_of_type(PokemonTypes.FIRE),
                                 SpecialConditions.BURNED),
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)