from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="33111e07-6f1b-51de-b5a2-1718d9bcdffe",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturneex.Name",
    display_name="Cacturne ex",
    searchable_by=["Cacturne ex", "Stage 1", "ex", "Cacturneex"],
    subtypes=["Stage 1", "ex"],
    collector_number=91,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Ability(
            title="Cursed Glare",
            game_text="As long as Cacturne ex is your Active Pok\u00e9mon, your opponent can't attach any Special Energy cards (except for Darkness and Metal Energy cards) from his or her hand to his or her Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Psybeam",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Spike Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)