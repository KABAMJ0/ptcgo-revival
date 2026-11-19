from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per, no_retreat_attack

card = PokemonCardDef(
    guid="cb644f4c-9f1b-5031-ab93-fbc85bc5767c",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantEX.Name",
    display_name="Trevenant-EX",
    searchable_by=["Trevenant-EX", "Basic", "EX", "TrevenantEX"],
    subtypes=["Basic", "EX"],
    collector_number=19,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=709,
    abilities=[
        Attack(
            title="Dark Forest",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Wood Blast",
            game_text="This attack does 20 more damage for each Grass Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.GRASS), per=20, base=50),
        ),
    ],
)