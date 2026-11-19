from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="bcd87518-3f57-5548-af1f-0a732004feea",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    display_name="Aron",
    searchable_by=["Aron", "Basic", "Aron"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=304,
    abilities=[
        Attack(
            title="Steel Tackle",
            game_text="Aron does 10 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10, damage=0),
        ),
    ],
)