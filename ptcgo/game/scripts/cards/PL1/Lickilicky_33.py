from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="54f75897-d0ad-5034-9216-22f24f79eca8",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name",
    display_name="Lickilicky",
    searchable_by=["Lickilicky", "Stage 1", "Lickilicky"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    family_id=108,
    abilities=[
        Attack(
            title="Harrumph",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Before doing damage, discard all Trainer cards attached to that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(40, pool="any", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Body Press",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            effect=unimplemented,
        ),
    ],
)