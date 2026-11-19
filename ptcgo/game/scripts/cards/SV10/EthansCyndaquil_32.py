from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="c6c99f38-9d61-598d-ad56-f08412c97214",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansCyndaquil.Name",
    display_name="Ethan's Cyndaquil",
    searchable_by=["Ethan's Cyndaquil", "Basic", "EthansCyndaquil"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=155,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)