from ptcgo.game.card_effects.attacks_common import damage_all_opponents
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="4a8c82d2-5b13-5506-a999-f68dc01bd86b",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic", "Nosepass"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="EX9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=299,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Wide Laser",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=damage_all_opponents(10),
        ),
    ],
)