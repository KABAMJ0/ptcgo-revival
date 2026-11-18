from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="f234127c-6733-5e6c-9cac-241f42226e1b",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganaclex.Name",
    display_name="Garganacl ex",
    searchable_by=["Garganacl ex", "Stage 2", "ex", "Garganaclex"],
    subtypes=["Stage 2", "ex"],
    collector_number=89,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=934,
    abilities=[
        Ability(
            title="Salty Body",
            game_text="This Pok\u00e9mon can't be affected by any Special Conditions.",
            effect=unimplemented,
        ),
        Attack(
            title="Block Hammer",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=protect_next_turn(reduce=60),
        ),
    ],
)