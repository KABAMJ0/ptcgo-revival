from ptcgo.game.card_effects.attacks_common import (
    count_energy, damage_per, self_energy_discard_attack,
)
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="931b5c37-b64f-52ab-881a-d5806b66fe0d",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Attack(
            title="The Third Eye",
            game_text="Discard an Energy card attached to Jirachi and draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=self_energy_discard_attack(count=1, also=draw_attack(3)),
        ),
        Attack(
            title="Psywave",
            game_text="Does 10 damage times the amount of Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("defender"), 10),
        ),
    ],
)