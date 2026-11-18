from ptcgo.game.card_effects.passives_common import condition_immunity_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="35ffbf69-e161-5d53-9a90-2d5f2ee8fe4a",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cameruptex.Name",
    display_name="Camerupt ex",
    searchable_by=["Camerupt ex", "Stage 1", "ex", "Cameruptex"],
    subtypes=["Stage 1", "ex"],
    collector_number=92,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Ability(title="Magma Armor", game_text="Camerupt ex can't be Asleep or Paralyzed.", passive=condition_immunity_passive([SpecialConditions.ASLEEP, SpecialConditions.PARALYZED])),
        Attack(
            title="Searing Flame",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Eruption",
            game_text="Each player discards the top card of his or her deck. This attack does 60 damage plus 20 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
