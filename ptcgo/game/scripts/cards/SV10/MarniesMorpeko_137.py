from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="5e24c67b-9794-5204-9c52-b1ad50758ba7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesMorpeko.Name",
    display_name="Marnie's Morpeko",
    searchable_by=["Marnie's Morpeko", "Basic", "MarniesMorpeko"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Spiky Wheel",
            game_text="This attack does 40 more damage for each Darkness Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.DARKNESS), per=40, base=20),
        ),
    ],
)